class StorageManager {
  constructor(prefix = 'app') {
    this.prefix = prefix;
  }

  _key(key) {
    return `${this.prefix}:${key}`;
  }

  set(key, value, ttl = null) {
    const item = {
      value,
      created: Date.now(),
      expires: ttl ? Date.now() + ttl * 1000 : null
    };
    localStorage.setItem(this._key(key), JSON.stringify(item));
  }

  get(key, defaultValue = null) {
    const raw = localStorage.getItem(this._key(key));
    if (!raw) return defaultValue;
    const item = JSON.parse(raw);
    if (item.expires && Date.now() > item.expires) {
      this.remove(key);
      return defaultValue;
    }
    return item.value;
  }

  remove(key) {
    localStorage.removeItem(this._key(key));
  }

  clear() {
    Object.keys(localStorage)
      .filter(k => k.startsWith(this.prefix + ':'))
      .forEach(k => localStorage.removeItem(k));
  }

  keys() {
    return Object.keys(localStorage)
      .filter(k => k.startsWith(this.prefix + ':'))
      .map(k => k.slice(this.prefix.length + 1));
  }

  size() {
    return this.keys().length;
  }
}

module.exports = StorageManager;
