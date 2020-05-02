class WebSocketService {
    static instance = null
    callbacks = {}
    
    constructor(){
        this.socketRef = null   
    }
    
    static getInstance() {
        if (!WebSocket.instance){
            WebSocket.instance = new WebSocket()
        }
        return WebSocket
    }

    connect(){
        const path = 'ws://127.0.0.1:8000/chat/lobby'
        this.socketRef = new WebSocket(path)
        this.socketRef.onopen = (e)=>{
            console.log("Web Socket Open")
        }
        this.socketRef.onmessage = (e) =>{
            console.log(e.message)
        }
        this.socketRef.onclose = (e)=>{
            console.log("Web Socket Closed")
        }
    }

    socketNewMessage(data){
        const parseData = JSON.parse(data)
        const command = parseData.command
        if (Object.keys(this.callbacks).length === 0) {
            return 
        }
        if (command==='messages'){
            this.callbacks[command](parseData.messages)
        }
        if (command === 'new_message'){
            this.callbacks[command](parseData.message)
        }
    }
    fetchMessages(username){
        this.sendMessage({command: 'fetch_messages', username: username })
    }
    newChatMessage(message){
        this.sendMessage({command: 'new_message', from: message.from, room: message.room, message: message.content })
    }
    addCallbacks(messagesCallback, newMessageCallback){
        this.callbacks['messages'] = messagesCallback;
        this.callbacks['new_message'] = newMessageCallback
    }
    sendMessage(data){
        try{
            this.socketRef.send(JSON.stringify({...data}))
        } catch(err){
            console.log(err.message)
        }
    }

    state(){
       return this.socketRef.readyState 
    }
}

const WebSocketInstance = WebSocketService.getInstance()

export default WebSocketInstance