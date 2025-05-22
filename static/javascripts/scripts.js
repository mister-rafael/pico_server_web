async function enviarComando() {
  await fetch('/api/comando', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ comando: "ligar_led" })
  });
}

async function buscarStatus() {
  const res = await fetch('/api/status');
  const data = await res.json();
  document.getElementById("temp").innerText = data.temperatura;
}

setInterval(buscarStatus, 5000); // Atualiza temperatura a cada 5s
