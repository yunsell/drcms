<template>
    <div class="row">

    <div class="col-6">
        <div class="card">
            <div class="card-header">
                <h3 class="card-title">콘텐츠 등록</h3>
            </div>
            <!-- /.card-header -->
            <div class="card-body">
                <table class="table table-bordered table-striped">

                <thead>
                    <tr>
                        <th>문단</th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(n, index) in msg" :key="index">
                  <td>{{n.paragraph}}</td>
                  </tr>
                </tbody>
                </table>
            </div>
            <!-- /.card-body -->
        </div>
        <!-- /.card -->
    </div>
    <!-- /.col -->

    <div class="col-6">
        <div class="card">
<!--            <div class="card-header">-->
<!--                <h3 class="card-title">콘텐츠 등록 (오른쪽)</h3>-->
<!--            </div>-->
            <!-- /.card-header -->
            <div class="card-body">
                <div class="row mb-3">
                    <div class="col-12">
                        <div class="float-right">
                            <button type="button" class="btn btn-primary">저장</button>
                            <button type="button" class="btn btn-default">내보내기</button>
                        </div>
                    </div>
                </div>

                <div class="row mb-3">
                    <div class="col-lg-2 col-sm-6 col-xs-12">
                        <input type="text" class="form-control"
                               name="contentType" id="contentType" placeholder="종류">
                    </div>
                    <div class="col-lg-2 col-sm-6 col-xs-12">
                        <input type="text" class="form-control"
                               name="clinic" id="clinic" placeholder="진료과목">
                    </div>
                    <div class="col-lg-2 col-sm-6 col-xs-12">
                        <input type="text" class="form-control"
                               name="clinicDiv" id="clinicDiv" placeholder="진료과목 분류">
                    </div>
                    <div class="col-lg-2 col-sm-6 col-xs-12">
                        <input type="text" class="form-control"
                               name="keyword" id="keyword" placeholder="키워드">
                    </div>
                    <div class="col-lg-2 col-sm-6 col-xs-12">
                        <input type="text" class="form-control"
                               name="hospital" id="hospital" placeholder="병원">
                    </div>
                    <div class="col-lg-2 col-sm-6 col-xs-12">
                        <input type="text" class="form-control"
                               name=source id="source" placeholder="출처">
                    </div>
                </div>

                <div class="row">
                    <div class="col-12">
                        <textarea name="contents" id="contents"
                                  class="form-control" rows="30"></textarea>
                    </div>
                </div>
            </div>
            <!-- /.card-body -->
        </div>
        <!-- /.card -->

    </div>
    <!-- /.col -->

</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ContentNew',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getTest() {
      const path = 'http://localhost:5000/v1.0/contentnew';
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

<style scoped>

</style>
