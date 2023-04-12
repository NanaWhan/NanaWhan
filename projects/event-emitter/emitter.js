class EventEmitter {
  constructor() {
    this.listeners = new Map();
    this.wildcardListeners = [];
  }

  on(event, callback) {
    if (event === '*') {
      this.wildcardListeners.push({ callback, once: false });
      return this;
    }
    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }
    this.listeners.get(event).push({ callback, once: false });
    return this;
  }

  once(event, callback) {
    if (event === '*') {
      this.wildcardListeners.push({ callback, once: true });
      return this;
    }
    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }
    this.listeners.get(event).push({ callback, once: true });
    return this;
  }

  emit(event, ...args) {
    const handlers = this.listeners.get(event) || [];
    handlers.forEach(h => h.callback(event, ...args));
    this.wildcardListeners.forEach(h => h.callback(event, ...args));

    this.listeners.set(event, handlers.filter(h => !h.once));
    this.wildcardListeners = this.wildcardListeners.filter(h => !h.once);
    return handlers.length > 0 || this.wildcardListeners.length > 0;
  }

  off(event, callback) {
    if (event === '*') {
      this.wildcardListeners = callback
        ? this.wildcardListeners.filter(h => h.callback !== callback)
        : [];
      return this;
    }
    if (!callback) {
      this.listeners.delete(event);
    } else {
      const handlers = this.listeners.get(event) || [];
      this.listeners.set(event, handlers.filter(h => h.callback !== callback));
    }
    return this;
  }

  listenerCount(event) {
    if (event === '*') return this.wildcardListeners.length;
    return (this.listeners.get(event) || []).length + this.wildcardListeners.length;
  }

  eventNames() {
    return [...this.listeners.keys()];
  }
}

module.exports = EventEmitter;
