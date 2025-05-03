import{$ as e,u as d,C as n,z as u}from"./main-C_QlMNZg.js";function r(l){let t=e("input[data-team-id]:checked").map(function(){return e(this).data("team-id")}),o=t.length===1?"team":"teams";d({title:"Delete Teams",body:`Are you sure you want to delete ${t.length} ${o}?`,success:function(){const a=[];for(var i of t)a.push(n.fetch(`/api/v1/teams/${i}`,{method:"DELETE"}));Promise.all(a).then(s=>{window.location.reload()})}})}function m(l){let t=e("input[data-team-id]:checked").map(function(){return e(this).data("team-id")});u({title:"ویرایش تیم",body:e(`
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
    `),button:"ارسال",success:function(){let o=e("#teams-bulk-edit").serializeJSON(!0);const a=[];for(var i of t)a.push(n.fetch(`/api/v1/teams/${i}`,{method:"PATCH",body:JSON.stringify(o)}));Promise.all(a).then(s=>{window.location.reload()})}})}e(()=>{e("#teams-delete-button").click(r),e("#teams-edit-button").click(m)});
