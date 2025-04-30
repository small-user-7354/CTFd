import "./main";
import $ from "jquery";
import { ezQuery } from "../compat/ezq";

function reset(event) {
  event.preventDefault();
  ezQuery({
    title: "CTF را دوباره تنظیم کنید؟",
    body: "آیا مطمئن هستید که می‌خواهید نمونه CTFd خود را بازنشانی کنید؟",
    success: function () {
      $("#reset-ctf-form").off("submit").submit();
    },
  });
}

$(() => {
  $("#reset-ctf-form").submit(reset);
});
