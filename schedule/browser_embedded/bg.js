// Runs inside the Facebook page: click Send, or fall back to pressing Enter.
function clickSend() {
  const btn = document.querySelector(
    '[aria-label="Press enter to send"], [aria-label="Send"], [aria-label="Odeslat"], [aria-label="Odoslať"], [aria-label="Stlačením klávesu Enter odošlete"]'
  );
  if (btn) {
    btn.click();
    return "clicked";
  }

  const box = document.querySelector('div[role="textbox"][contenteditable="true"]');
  if (!box) return "no textbox";
  box.focus();
  const o = { key: "Enter", code: "Enter", keyCode: 13, which: 13, bubbles: true };
  box.dispatchEvent(new KeyboardEvent("keydown", o));
  box.dispatchEvent(new KeyboardEvent("keyup", o));
  return "enter sent";
}

chrome.alarms.onAlarm.addListener(async (alarm) => {
  if (alarm.name !== "send") return;
  const { job } = await chrome.storage.local.get("job");
  if (!job) return;

  try {
    const [res] = await chrome.scripting.executeScript({
      target: { tabId: job.tabId },
      func: clickSend,
    });
    console.log("Result:", res?.result);
  } catch (e) {
    console.error("Send failed (tab closed?)", e);
  }
  await chrome.storage.local.remove("job");
});
