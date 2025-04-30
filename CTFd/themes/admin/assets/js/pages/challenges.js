import "./main";
import CTFd from "../compat/CTFd";
import $ from "jquery";
import "../compat/json";
import { ezAlert, ezQuery } from "../compat/ezq";

function deleteSelectedChallenges(_event) {
  let challengeIDs = $("input[data-challenge-id]:checked").map(function () {
    return $(this).data("challenge-id");
  });
  let target = challengeIDs.length === 1 ? "challenge" : "challenges";

  ezQuery({
    title: "حذف چالش‌ها",
    body: `آیا مطمئنید که میخواهید چالش را حذف کنید؟ ${challengeIDs.length} ${target}?`,
    success: function () {
      const reqs = [];
      for (var chalID of challengeIDs) {
        reqs.push(
          CTFd.fetch(`/api/v1/challenges/${chalID}`, {
            method: "DELETE",
          }),
        );
      }
      Promise.all(reqs).then((_responses) => {
        window.location.reload();
      });
    },
  });
}

function bulkEditChallenges(_event) {
  let challengeIDs = $("input[data-challenge-id]:checked").map(function () {
    return $(this).data("challenge-id");
  });

  ezAlert({
    title: "ویرایش چالش‌ها",
    body: $(`
    <form id="challenges-bulk-edit">
      <div class="form-group">
        <label>کتگوری</label>
        <input type="text" name="category" data-initial="" value="">
      </div>
      <div class="form-group">
        <label>مقدار</label>
        <input type="number" name="value" data-initial="" value="">
      </div>
      <div class="form-group">
        <label>حالت</label>
        <select name="state" data-initial="">
          <option value="">--</option>
          <option value="visible">قابل مشاهده</option>
          <option value="hidden">پنهان</option>
        </select>
      </div>
    </form>
    `),
    button: "ارسال",
    success: function () {
      let data = $("#challenges-bulk-edit").serializeJSON(true);
      const reqs = [];
      for (var chalID of challengeIDs) {
        reqs.push(
          CTFd.fetch(`/api/v1/challenges/${chalID}`, {
            method: "PATCH",
            body: JSON.stringify(data),
          }),
        );
      }
      Promise.all(reqs).then((_responses) => {
        window.location.reload();
      });
    },
  });
}

$(() => {
  $("#challenges-delete-button").click(deleteSelectedChallenges);
  $("#challenges-edit-button").click(bulkEditChallenges);
});
