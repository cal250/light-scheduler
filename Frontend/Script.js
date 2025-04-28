const socket = new WebSocket('ws://localhost:8765'); // WebSocket server URL
const statusDiv = document.getElementById('status');

socket.onopen = () => {
  console.log('WebSocket connection established.');
};

socket.onerror = (error) => {
  console.error('WebSocket Error:', error);
};

document.getElementById('scheduleForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const onTime = document.getElementById('onTime').value;
  const offTime = document.getElementById('offTime').value;
  const message = JSON.stringify({ on_time: onTime, off_time: offTime });
  
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(message);
    statusDiv.textContent = "✅ Schedule sent successfully!";
    statusDiv.style.color = "green";
  } else {
    statusDiv.textContent = "❌ WebSocket not connected!";
    statusDiv.style.color = "red";
  }
});
