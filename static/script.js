async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const userMsg = input.value.trim();
    if (!userMsg) return;

    chatBox.innerHTML += `<div class='user'>🧑 You: ${userMsg}</div>`;
    input.value = "";

    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMsg })
    });

    const data = await res.json();
    chatBox.innerHTML += `<div class='bot'>🤖 Bot: ${data.reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    // Speak bot response
    const synth = window.speechSynthesis;
    const utter = new SpeechSynthesisUtterance(data.reply);
    synth.speak(utter);
}

function startVoice() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        document.getElementById("user-input").value = text;
        sendMessage();
    };
}
