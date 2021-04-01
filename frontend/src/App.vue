<template>
  <div>
      <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand v-b-toggle.sidebar-no-header href="/">Dr CMS</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/content">콘텐츠 목록</b-nav-item>
        <b-nav-item href="/contentnew">콘텐츠 등록</b-nav-item>
        <b-nav-item href="/upload">콘텐츠 업로드</b-nav-item>
        <b-nav-item href="/user">사용자 목록</b-nav-item>
        <b-nav-item href="/new">사용자 등록</b-nav-item>
    <b-nav-item v-b-toggle.sidebar-backdrop>Sidebar Test</b-nav-item>
    <b-sidebar id="sidebar-backdrop" aria-labelledby="sidebar-no-header-title" backdrop shadow>
      <template #default="{ hide }">
        <div class="p-3">
          <h4 id="sidebar-no-header-title">Custom header sidebar</h4>
          <p>
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
            in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
          </p>
          <b-button href="/content" block @click="hide">콘텐츠 목록</b-button>
          <b-button href="/contentnew" block @click="hide">콘텐츠 등록</b-button>
          <b-button href="/upload" block @click="hide">콘텐츠 업로드</b-button>
          <br>
          <b-button variant="info" href="/user" block @click="hide">사용자 목록</b-button>
          <b-button variant="info" href="/new" block @click="hide">사용자 등록</b-button>

        </div>
      </template>
    </b-sidebar>

      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

        <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">ES</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">FA</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

</style>
