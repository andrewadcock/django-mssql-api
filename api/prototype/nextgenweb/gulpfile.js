var gulp = require('gulp');
gulp.task('default', function () {
  gulp.src('./node_modules/@cmsgov/design-system-core/dist/index.css')
   .pipe(gulp.dest('./dist/assets/core/'));
   gulp.src('./node_modules/@cmsgov/design-system-layout/dist/index.css')
   .pipe(gulp.dest('./dist/assets/layout/'));
});

//gulp.task('default');