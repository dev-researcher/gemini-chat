import React, { useState } from 'react';
import axios from 'axios';

function ChatApp() {
    const [input, setInput] = useState('');
    const [response, setResponse] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const result = await axios.post('/api/chat', { prompt: input });
            setResponse(result.data.response);
        } catch (error) {
            console.error("Error fetching response: ", error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input 
                    type="text" 
                    value={input} 
                    onChange={(e) => setInput(e.target.value)} 
                />
                <button type="submit">Send</button>
            </form>
            <div>{response}</div>
        </div>
    );
}

export default ChatApp;