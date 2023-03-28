class EventEmitter {
  constructor() {
    this.listeners = new Map();
  }

  on(event, callback) {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }
    this.listeners.get(event).push({ callback, once: false });
    return this;
  }

  once(event, callback) {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }
    this.listeners.get(event).push({ callback, once: true });
    return this;
  }

  emit(event, ...args) {
    const handlers = this.listeners.get(event) || [];
    handlers.forEach(handler => handler.callback(...args));
    this.listeners.set(event, handlers.filter(h => !h.once));
    return handlers.length > 0;
  }

  off(event, callback) {
    if (!callback) {
      this.listeners.delete(event);
    } else {
      const handlers = this.listeners.get(event) || [];
      this.listeners.set(event, handlers.filter(h => h.callback !== callback));
    }
    return this;
  }

  listenerCount(event) {
    return (this.listeners.get(event) || []).length;
  }
}

module.exports = EventEmitter;
