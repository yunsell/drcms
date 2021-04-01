<template>
  <div class="card-header">
    <h3 class="card-title">사용자 목록</h3>
    <hr>
      <b-nav-form>
      <b-form-input class="mr-sm-2" placeholder="Search" v-model="searchName"></b-form-input>
      <b-button variant="outline-success" class="my-2 my-sm-0" type="submit">Search</b-button>
      </b-nav-form>
  <br>
  <table class="table table-striped table-hover">
    <thead>
      <tr>
        <th scope='col'>Email</th>
        <th scope='col'>User</th>
        <th scope='col'>등급</th>
        <th scope='col'>가입일자</th>
        <th scope='col'>수정 / 삭제</th>
      </tr>
    </thead>
  <tbody>
    <tr v-for="(n, index) in msg" :key="index" v-show="n.user_name.includes(searchName)">
      <td>{{n.email}}</td>
      <td>{{n.user_name}}</td>
      <td>{{n.grade}}</td>
      <td>{{n.created_at}}</td>
        <td>
        <div class="btn-group" role="group">
          <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  @click="edit()">
              Update
          </button>
          <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDelete()">
              Delete
          </button>
        </div>
        </td>
    </tr>
  </tbody>
</table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'User',
  data() {
    return {
      msg: '',
      searchName: '',
    };
  },
  methods: {
    getTest() {
      const path = 'http://localhost:5000/v1.0/user';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getTest();
  },
};
</script>
