import{$ as s,C as n,z as l}from"./main-C_QlMNZg.js";const d={users:(e,a)=>n.api.patch_user_public({userId:e},a),teams:(e,a)=>n.api.patch_team_public({teamId:e},a)};function u(){const e=s(this),a=e.data("account-id"),i=e.data("state");let t;i==="visible"?t=!0:i==="hidden"&&(t=!1);const o={hidden:t};d[n.config.userMode](a,o).then(c=>{c.success&&(t?(e.data("state","hidden"),e.addClass("btn-danger").removeClass("btn-success"),e.text("Hidden")):(e.data("state","visible"),e.addClass("btn-success").removeClass("btn-danger"),e.text("Visible")))})}function r(e,a){const i={hidden:a==="hidden"},t=[];for(let o of e.accounts)t.push(d[n.config.userMode](o,i));for(let o of e.users)t.push(d.users(o,i));Promise.all(t).then(o=>{window.location.reload()})}function b(e){let a=s(".tab-pane.active input[data-account-id]:checked").map(function(){return s(this).data("account-id")}),i=s(".tab-pane.active input[data-user-id]:checked").map(function(){return s(this).data("user-id")}),t={accounts:a,users:i};l({title:"قابلیت دیدن",body:s(`
    <form id="scoreboard-bulk-edit">
      <div class="form-group">
        <label>قابلیت دیدن</label>
        <select name="visibility" data-initial="">
          <option value="">--</option>
          <option value="visible">قابل دیدن</option>
          <option value="hidden">پنهان</option>
        </select>
      </div>
    </form>
    `),button:"ارسال",success:function(){let c=s("#scoreboard-bulk-edit").serializeJSON(!0).visibility;r(t,c)}})}s(()=>{s(".scoreboard-toggle").click(u),s("#scoreboard-edit-button").click(b)});
