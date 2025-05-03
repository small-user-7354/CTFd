import "./main";
import CTFd from "../compat/CTFd";
import $ from "jquery";
import "../compat/json";
import { ezAlert, ezQuery } from "../compat/ezq";

function deleteSelectedTeams(_event) {
  let teamIDs = $("input[data-team-id]:checked").map(function () {
    return $(this).data("team-id");
  });
  let target = teamIDs.length === 1 ? "team" : "teams";

  ezQuery({
    title: "Delete Teams",
    body: `Are you sure you want to delete ${teamIDs.length} ${target}?`,
    success: function () {
      const reqs = [];
      for (var teamID of teamIDs) {
        reqs.push(
          CTFd.fetch(`/api/v1/teams/${teamID}`, {
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

function bulkEditTeams(_event) {
  let teamIDs = $("input[data-team-id]:checked").map(function () {
    return $(this).data("team-id");
  });

  ezAlert({
    title: "ویرایش تیم",
    body: $(`
    <form id="teams-bulk-edit">
      <div class="form-group my-3">
        <label>بن شده</label>
        <select name="banned" data-initial="">
          <option value="">--</option>
          <option value="true">بله</option>
          <option value="false">خیر</option>
        </select>
      </div>
      <div class="form-group my-3">
        <label>پنهان</label>
        <select name="hidden" data-initial="">
          <option value="">--</option>
          <option value="true">بله</option>
          <option value="false">خیر</option>
        </select>
      </div>
    </form>
    `),
    button: "ارسال",
    success: function () {
      let data = $("#teams-bulk-edit").serializeJSON(true);
      const reqs = [];
      for (var teamID of teamIDs) {
        reqs.push(
          CTFd.fetch(`/api/v1/teams/${teamID}`, {
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
  $("#teams-delete-button").click(deleteSelectedTeams);
  $("#teams-edit-button").click(bulkEditTeams);
});
