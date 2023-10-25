function debounce(fn, delay) {
  let timer = null;
  const debounced = function (...args) {
    clearTimeout(timer);
    return new Promise((resolve) => {
      timer = setTimeout(() => resolve(fn.apply(this, args)), delay);
    });
  };
  debounced.cancel = () => clearTimeout(timer);
  return debounced;
}

function throttle(fn, limit) {
  let inThrottle = false;
  let lastArgs = null;
  const throttled = function (...args) {
    if (!inThrottle) {
      fn.apply(this, args);
      inThrottle = true;
      setTimeout(() => {
        inThrottle = false;
        if (lastArgs) {
          throttled.apply(this, lastArgs);
          lastArgs = null;
        }
      }, limit);
    } else {
      lastArgs = args;
    }
  };
  throttled.cancel = () => { inThrottle = false; lastArgs = null; };
  return throttled;
}

function retry(fn, maxAttempts = 3, delay = 1000) {
  return async function (...args) {
    for (let i = 0; i < maxAttempts; i++) {
      try {
        return await fn.apply(this, args);
      } catch (err) {
        if (i === maxAttempts - 1) throw err;
        await new Promise(r => setTimeout(r, delay * Math.pow(2, i)));
      }
    }
  };
}

module.exports = { debounce, throttle, retry };
