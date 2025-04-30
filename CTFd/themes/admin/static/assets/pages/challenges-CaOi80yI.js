import{$ as e,u as c,C as i,z as d}from"./main-C_QlMNZg.js";function u(o){let l=e("input[data-challenge-id]:checked").map(function(){return e(this).data("challenge-id")}),a=l.length===1?"challenge":"challenges";c({title:"حذف چالش‌ها",body:`آیا مطمئنید که میخواهید چالش را حذف کنید؟ ${l.length} ${a}?`,success:function(){const t=[];for(var n of l)t.push(i.fetch(`/api/v1/challenges/${n}`,{method:"DELETE"}));Promise.all(t).then(s=>{window.location.reload()})}})}function r(o){let l=e("input[data-challenge-id]:checked").map(function(){return e(this).data("challenge-id")});d({title:"ویرایش چالش‌ها",body:e(`
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
    `),button:"ارسال",success:function(){let a=e("#challenges-bulk-edit").serializeJSON(!0);const t=[];for(var n of l)t.push(i.fetch(`/api/v1/challenges/${n}`,{method:"PATCH",body:JSON.stringify(a)}));Promise.all(t).then(s=>{window.location.reload()})}})}e(()=>{e("#challenges-delete-button").click(u),e("#challenges-edit-button").click(r)});
