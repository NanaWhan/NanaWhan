class Stopwatch {
  constructor() {
    this.startTime = null;
    this.elapsed = 0;
    this.laps = [];
    this.running = false;
  }

  start() {
    if (!this.running) {
      this.startTime = Date.now() - this.elapsed;
      this.running = true;
    }
  }

  stop() {
    if (this.running) {
      this.elapsed = Date.now() - this.startTime;
      this.running = false;
    }
    return this.elapsed;
  }

  lap() {
    const current = this.running ? Date.now() - this.startTime : this.elapsed;
    const lastLap = this.laps.length > 0 ? this.laps[this.laps.length - 1].total : 0;
    this.laps.push({ split: current - lastLap, total: current });
    return this.laps[this.laps.length - 1];
  }

  reset() {
    this.startTime = null;
    this.elapsed = 0;
    this.laps = [];
    this.running = false;
  }

  format(ms) {
    const mins = Math.floor(ms / 60000);
    const secs = Math.floor((ms % 60000) / 1000);
    const millis = ms % 1000;
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}.${String(millis).padStart(3, '0')}`;
  }
}

module.exports = Stopwatch;
