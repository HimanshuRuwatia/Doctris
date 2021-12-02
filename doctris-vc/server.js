const express = require("express");
const {v4 : uuidv4} = require('uuid');

const app = express();

const server = require("http").Server(app);

const io = require('socket.io')(server);

const {ExpressPeerServer} = require ('peer');
const peerServer = ExpressPeerServer(server, {
  debug:true
});

app.use(express.static('public'));

app.set('view engine','ejs');
app.use(express.urlencoded({extended: false}));

app.use("/meet/peerjs", peerServer)

app.get("/", (req,res) => {
  res.render("index");
});

app.get("/meet", (req,res) => {
  res.redirect(`/meet/${uuidv4()}`);
});

app.get("/meet/:room", (req,res) => {
  res.render("room", { roomId: req.params.room });
});

io.on('connection', socket => {
  socket.on('join-room', (roomId, userId) => {
    socket.join(roomId);
    socket.to(roomId).broadcast.emit('user-connected', userId);
    socket.on('message', (message, sender) => {
      io.to(roomId).emit('createMessage', message, sender);
    });

    socket.on('disconnect', () => {
      socket.to(roomId).broadcast.emit('user-disconnected', userId)
    });
  });
});

server.listen(process.env.PORT || 3000);
