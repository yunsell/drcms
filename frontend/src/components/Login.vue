<template>
  <div>
    <div class="header bg-gradient-success py-7 py-lg-8 pt-lg-9">
    <b-container class="container">
      <div class="header-body text-center mb-7">
        <b-row class="justify-content-center">
          <b-col xl="5" lg="6" md="8" class="px-5">
            <h1 class="text-black">Create an account</h1>
              <p class="text-lead text-black">Use these awesome forms</p>
          </b-col>
        </b-row>
      </div>
        <b-card-header class="bg-transparent pb-5">
          <div class="text-muted text-center mt-2 mb-4"><small>Sign up with</small></div>
            <div class="text-center">
              <a href="#" class="btn btn-neutral btn-icon mr-4">
                <span class="btn-inner--icon"><img src="../../public/icon/github.svg"></span>
                <span class="btn-inner--text">Github</span>
                </a>
                <a href="#" class="btn btn-neutral btn-icon">
                  <span class="btn-inner--icon"><img src="../../public/icon/google.svg"></span>
                  <span class="btn-inner--text">Google</span>
              </a>
          </div>
        </b-card-header>
    </b-container>
    <div class="separator separator-bottom separator-skew zindex-100">
      <svg x="0" y="0" viewBox="0 0 2560 100" preserveAspectRatio="none" version="1.1"
             xmlns="http://www.w3.org/2000/svg">
        </svg>
      </div>
    </div>
    <b-container class="container">
      <div class="p-4 bg-secondary">
      <b-input placeholder="Email" class="form-control-alternative mb-3"/>
      <b-input placeholder="Name" class="form-control-alternative mb-3"/>
      <b-input placeholder="Password" class="form-control-alternative mb-3"/>
      </div>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getTest() {
      const path = 'http://localhost:5000/';
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
