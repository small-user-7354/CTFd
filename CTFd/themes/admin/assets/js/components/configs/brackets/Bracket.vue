<template>
  <div class="border-bottom">
    <div>
      <button
        type="button"
        class="close float-right"
        aria-label="Close"
        @click="deleteBracket()"
      >
        <span aria-hidden="true">&times;</span>
      </button>
    </div>

    <div class="row">
      <div class="col-md-9">
        <div class="form-group my-3">
          <label>نام براکت</label>
          <input type="text" class="form-control" v-model.lazy="bracket.name" />
          <small class="form-text text-muted">
            نام براکت (مثلاً «دانشجویان»، «کارآموزان»، «مهندسان»)
          </small>
        </div>
      </div>

      <div class="col-md-12">
        <div class="form-group my-3">
          <label>شرح براکت</label>
          <input
            type="text"
            class="form-control"
            v-model.lazy="bracket.description"
          />
          <small class="form-text text-muted">شرح براکت</small>
        </div>
      </div>

      <div class="col-md-12">
        <label>نوع براکت</label>
        <select class="custom-select" v-model.lazy="bracket.type">
          <option></option>
          <option value="users">کاربران</option>
          <option value="teams">تیم‌ها</option>
        </select>
        <small class="form-text text-muted">
           اگر از حالت تیمی استفاده می‌کنید و می‌خواهید این براکت به جای افراد، برای کل تیم‌ها اعمال شود، گزینه تیم‌ها را انتخاب کنید.
        </small>
      </div>
    </div>

    <div class="row py-3">
      <div class="col-md-12">
        <div class="d-block py-3">
          <button
            class="btn btn btn-success btn-outlined float-right"
            type="button"
            @click="saveBracket()"
          >
            ذخیره
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CTFd from "../../../compat/CTFd";
import { ezToast } from "../../../compat/ezq";

export default {
  props: {
    index: Number,
    initialBracket: Object,
  },
  data: function () {
    return {
      bracket: this.initialBracket,
    };
  },
  methods: {
    persisted: function () {
      // We're using Math.random() for unique IDs so new items have IDs < 1
      // Real items will have an ID > 1
      return this.bracket.id >= 1;
    },
    saveBracket: function () {
      let body = this.bracket;
      let url = "";
      let method = "";
      let message = "";
      if (this.persisted()) {
        url = `/api/v1/brackets/${this.bracket.id}`;
        method = "PATCH";
        message = "Bracket has been updated!";
      } else {
        url = `/api/v1/brackets`;
        method = "POST";
        message = "Bracket has been created!";
      }
      CTFd.fetch(url, {
        method: method,
        credentials: "same-origin",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      })
        .then((response) => {
          return response.json();
        })
        .then((response) => {
          if (response.success === true) {
            this.bracket = response.data;
            ezToast({
              title: "Success",
              body: message,
              delay: 1000,
            });
          }
        });
    },
    deleteBracket: function () {
      if (confirm("Are you sure you'd like to delete this bracket?")) {
        if (this.persisted()) {
          CTFd.fetch(`/api/v1/brackets/${this.bracket.id}`, {
            method: "DELETE",
            credentials: "same-origin",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
          })
            .then((response) => {
              return response.json();
            })
            .then((response) => {
              if (response.success === true) {
                this.$emit("remove-bracket", this.index);
              }
            });
        } else {
          this.$emit("remove-bracket", this.index);
        }
      }
    },
  },
};
</script>
