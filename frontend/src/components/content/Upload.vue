<template>
    <div class="row">

    <div class="col-12">
        <div class="card card-primary">
            <div class="card-header">
                <h3 class="card-title">콘텐츠 파일 업로드</h3>
            </div>
            <!-- form start -->
            <form role="form" method="post" enctype="multipart/form-data" action="">
            <div class="card-body">
                <div class="form-group">
                    <label for="documentFile">문서 파일</label>
                    <b-form-file id="file-default"></b-form-file>
<!--                    <div class="custom-file">-->
<!--                        <input type="file" class="custom-file-input"-->
<!--                               name="documentFile" id="documentFile" required>-->
<!--                        <label class="custom-file-label">파일 선택</label>-->
<!--                    </div>-->
                </div>
            </div>
            <div class="card-footer">
                <b-button type="submit" variant="outline-primary">업로드</b-button>
            </div>
            </form>
        </div>
    </div>

</div>

</template>

<script>
export default {
  name: 'upload',
};
</script>

<style scoped>

</style>
