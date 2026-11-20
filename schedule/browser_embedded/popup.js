const statusEl = document.getElementById("status");

function showJob(job) {
  statusEl.textContent = job
    ? "Naplánované: " + new Date(job.when).toLocaleString("sk-SK")
    : "Nič nie je naplánované";
}

chrome.storage.local.get("job", ({ job }) => showJob(job));

document.getElementById("schedule").onclick = async () => {
  const when = new Date(document.getElementById("when").value).getTime();
  if (!when || when <= Date.now()) {
    statusEl.textContent = "Vyberte čas v budúcnosti";
    return;
  }

  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab || !/^https:\/\/www\.(facebook|messenger)\.com\//.test(tab.url || "")) {
    statusEl.textContent = "Najprv otvorte konverzáciu na Facebooku/Messengeri";
    return;
  }

  const job = { tabId: tab.id, when };
  await chrome.storage.local.set({ job });
  await chrome.alarms.create("send", { when });
  showJob(job);
};

document.getElementById("cancel").onclick = async () => {
  await chrome.alarms.clear("send");
  await chrome.storage.local.remove("job");
  statusEl.textContent = "Zrušené";
};
