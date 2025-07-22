// let cpuCount = 4;

const updateCPU = async () => {
	const res = await fetch('/cpu');
	const data = await res.json();

	const cpuUsage = data.cpu_usage_per_core;
	const cpuCount = data.total_cores;

	const cpuBars = document.querySelectorAll('.bar-graph-wrapper');
	for (let i = 0; i < cpuCount; i++) {
		const cpuBar = cpuBars[i];
		const usage = cpuUsage[i];
		cpuBar.style.background = `linear-gradient(90deg, var(--graph-green) 0%, var(--graph-green) ${usage}%, var(--graph-background) ${usage}%, var(--graph-background) 100%`;
	}

	requestAnimationFrame(updateCPU);
}

const updateRAM = async () => {
	const res = await fetch('/memory');
	const data = await res.json();

	const usage = data.memory_percentage;

	const bar = document.querySelector('#ram-graph');
	bar.style.background = `linear-gradient(0deg, var(--graph-green) 0%, var(--graph-green) ${usage}%, var(--graph-background) ${usage}%, var(--graph-background) 100%`;

	requestAnimationFrame(updateRAM);
}

const clockDOM = document.querySelector('#clock');
const updateClock = async () => {
	const now = new Date();
	const h = now.getHours();
	const m = `${now.getMinutes()}`.padStart(2, '0');

	clockDOM.innerText = h + ':' + m;

	requestAnimationFrame(updateClock);
}

updateCPU();
updateRAM();
updateClock();