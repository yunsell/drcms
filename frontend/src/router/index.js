import Vue from 'vue';
import Router from 'vue-router';
import Login from '../components/Login.vue';

import Content from '../components/content/Content.vue';
import Upload from '../components/content/Upload.vue';
import ContentNew from '../components/content/ContentNew.vue';

import User from '../components/user/User.vue';
import New from '../components/user/New.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login,
    },
    {
      path: '/user',
      name: 'User',
      component: User,
    },
    {
      path: '/content',
      name: 'Content',
      component: Content,
    },
    {
      path: '/upload',
      name: 'Upload',
      component: Upload,
    },
    {
      path: '/new',
      name: 'New',
      component: New,
    },
    {
      path: '/contentnew',
      name: 'ContentNew',
      component: ContentNew,
    },
  ],
});
