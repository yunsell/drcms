<template>
  <div class="row">
    <div class="col-12">
        <div class="card card-primary">
            <div class="card-header">
                <h3 class="card-title">사용자 신규 등록</h3>
            </div>
            <!-- /.card-header -->
            <!-- form start -->
            <form role="form" method="post" action="">
            <div class="card-body">
                <div class="form-group">
                    <label for="email">이메일</label>
                    <input type="email" class="form-control"
                           name="email" id="email" placeholder="이메일" required>
                </div>
                <div class="form-group">
                    <label for="userName">이름</label>
                    <input type="text" class="form-control"
                           name="userName" id="userName" placeholder="이름" required>
                </div>
                <div class="form-group">
                    <label for="password">비밀번호</label>
                    <input type="password" class="form-control"
                           name="password" id="password" placeholder="비밀번호"
                           minlength="6" autocomplete="new-password">
                </div>
                <div class="form-group">
                    <label for="shops">매장목록</label>
                    <select name="shops" id="shops" class="form-control select2"
                            multiple="multiple" data-placeholder="매장목록">
                    </select>
                </div>
            </div>
            <!-- /.card-body -->

            <div class="card-footer">
                <b-button type="submit" variant="outline-primary">등록</b-button>
            </div>
            </form>
        </div>
        <!-- /.card -->
    </div>
    <!-- /.col -->

</div>
</template>
