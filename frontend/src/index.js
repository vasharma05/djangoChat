import React from 'react';
import ReactDOM from 'react-dom'
import WebSocketInstance from "./WebSocket"

class App extends React.Component{
    constructor(){
        currentUser = 'vineet'
        super()
        this.state = {}
        this.waitForSocketConnection(()=>{
            WebSocketInstance.addCallbacks(
                this.setMessages.bind(this),
                this.addMessage.bind(this)
            )
            WebSocketInstance.fetchMessages(this.CurrentUser)
        })
    }
    waitForSocketConnection(callback){
        const component = this
        setTimeout(
            function(){
                if (WebSocketInstance.state() === 1){
                    console.log('Connection Secure')
                }
            }
        )
    }
    render(){
        return(
            <div>
                <textarea id="chat-log" cols="100" rows="20" readonly></textarea><br />
                <input id="chat-message-input" type="text" size="100" /><br />
                <input id="chat-message-submit" type="button" value="Send"/>
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('root'))