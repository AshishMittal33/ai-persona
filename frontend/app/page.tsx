'use client'

import { useState } from 'react'

export default function Home() {

  const [message, setMessage] = useState('')
  const [reply, setReply] = useState('')

  async function sendMessage() {

    const response = await fetch(
      'http://127.0.0.1:8000/chat',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: message
        })
      }
    )

    const data = await response.json()

    setReply(data.reply)
  }

  return (
    <div style={{ padding: '20px' }}>

      <h1>AI Persona</h1>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask something..."
      />

      <button onClick={sendMessage}>
        Send
      </button>

      <hr />

      <p>{reply}</p>

    </div>
  )
}