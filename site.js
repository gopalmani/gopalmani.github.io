(() => {
  "use strict";
  const clock = document.getElementById("india-clock");
  const date = document.getElementById("clock-date");
  const year = document.getElementById("year");
  const timeFormat = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Asia/Kolkata", hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23",
  });
  const dateFormat = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Asia/Kolkata", day: "2-digit", month: "short", year: "numeric",
  });
  function tick() {
    const now = new Date();
    if (clock) {
      clock.textContent = timeFormat.format(now);
      clock.dateTime = now.toISOString();
    }
    if (date) date.textContent = `${dateFormat.format(now)} · IST / UTC+05:30`;
    if (year) year.textContent = String(now.getFullYear());
  }
  tick();
  // Read the wall clock each tick; never accumulate drift or announce every second.
  window.setInterval(() => { if (!document.hidden) tick(); }, 1000);
  document.addEventListener("visibilitychange", () => { if (!document.hidden) tick(); });
})();
