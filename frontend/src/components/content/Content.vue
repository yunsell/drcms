<template>
    <div class="card-header">
      <h3 class="card-title">콘텐츠 목록</h3>
  <hr>
      <b-nav-form>
      <b-form-input class="mr-sm-2" placeholder="Search" v-model="search"></b-form-input>
      <b-button variant="outline-success" class="my-2 my-sm-0" type="submit">Search</b-button>
      </b-nav-form>
  <br>
  <table class="table table-hover">
    <thead>
      <tr>
        <th scope='col'>제목</th>
        <th scope='col'>종류</th>
        <th scope='col'>진료과목</th>
        <th scope='col'>분류</th>
        <th scope='col'>키워드</th>
        <th scope='col'>병원</th>
        <th scope='col'>출처</th>
        <th scope='col'>작성자</th>
        <th scope='col'>등록일시</th>
        <th scope='col'>수정일시</th>
        <th scope='col'>수정/삭제</th>
      </tr>
    </thead>
  <tbody>
    <tr v-for="(n, index) in msg" :key="index" v-show="n.title.includes(search)">
      <td>{{n.title}}</td>
      <td>{{n.contentType}}</td>
      <td>{{n.clinic}}</td>
      <td>{{n.clinicDiv}}</td>
      <td>{{n.keyword}}</td>
      <td>{{n.hospital}}</td>
      <td>{{n.source}}</td>
      <td>{{n.registerUserName}}</td>
      <td>{{n.createdAt}}</td>
      <td>{{n.updatedAt}}</td>
        <td>
        <div class="btn-group" role="group">
          <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.book-update-modal
                  @click="editBook(book)">
              Update
          </button>
          <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteBook(book)">
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
  name: 'Content',
  data() {
    return {
      msg: '',
      search: '',
    };
  },
  methods: {
    getTest() {
      const path = 'http://localhost:5000/v1.0/content';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getTest();
  },
};
</script>
