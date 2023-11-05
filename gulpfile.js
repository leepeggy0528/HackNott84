const {
    src,
    dest,
    series,
    parallel,
    watch
} = require('gulp');

function taskcon(cb) {
    console.log('hello gulp4 WA HA HA HA');
    cb(); //告知任務結束
}
//任務輸出 exports.任務名稱 = function
// print cmd
exports.console = taskcon;

function taskA(cb) {
    console.log('任務A');
    cb();
}

function taskB(cb) {
    console.log('任務B');
    cb();
}

//同步
exports.a = series(taskA, taskB);//依序執行
exports.b = parallel(taskA, taskB);//同時執行

//壓縮照片
const imagemin = require('gulp-imagemin');

function imgmin() {
    return src('src/images/*.*')
        .pipe(imagemin([
            imagemin.mozjpeg({ quality: 70, progressive: true })
            // 壓縮品質 quality越低 -> 壓縮越大 -> 品質越差 
        ]))
        .pipe(dest('dist/images'))
}

exports.img = imgmin;

//圖片搬家
function moveimg() {
    return src(['src/images/*.*', 'src/images/**/*.*']).pipe(dest('dist/images'));
}

//SASS
const sass = require('gulp-sass')(require('sass'));
const sourcemaps = require('gulp-sourcemaps');
const cleanCSS = require('gulp-clean-css');
const autoprefixer = require('gulp-autoprefixer');

function sassstyle() {
    return src('./src/sass/*.scss') //來源檔案
        .pipe(sourcemaps.init())
        .pipe(sass.sync().on('error', sass.logError))// sass編譯
        .pipe(autoprefixer())
        // .pipe(cleanCSS({compatibility: 'ie10'})) //壓縮css 
        .pipe(sourcemaps.write())//寫入sourcemaps
        .pipe(dest('dist/css'))// 目的地檔案
}

exports.sass = sassstyle;

// html template
const fileinclude = require('gulp-file-include');

function includeHTML() {
    return src('src/*.html')
        .pipe(fileinclude({
            prefix: '@@',
            basepath: '@file'
        }))
        .pipe(dest('dist'));
}
exports.html = includeHTML;

// JS
const uglify = require('gulp-uglify');
const babel = require('gulp-babel');

function ugjs() {
    return src('src/js/*.js')
        .pipe(uglify())
        .pipe(babel({
            presets: ['@babel/env']
        }))// es6 -> es5
        .pipe(dest('dist/js'))
}

exports.ug = ugjs

//python
function pyth() {
    return src('src/*.py').pipe(dest('dist'))
}
exports.py = pyth

function pycog() {
    return src('src/cofig/*.toml').pipe(dest('dist/cofig'))
}
exports.pyg = pycog

//監看
function watchsass() {
    watch(['./src/sass/*.scss', './src/sass/**/*.scss'], sassstyle); // ** 第二層路徑
    watch(['src/*.html', 'src/layout/*.html'], includeHTML); // ** 第二層路徑
    watch('src/js/*.js', ugjs); // ** 第二層路徑
}

exports.w = watchsass;

//同步瀏覽
const browserSync = require('browser-sync');
const reload = browserSync.reload;


function browser(done) {
    browserSync.init({
        server: {
            baseDir: "./dist",
            index: "index.html"
        },
        port: 3000
    });
    watch(['./src/sass/*.scss', './src/sass/**/*.scss'], sassstyle).on('change', reload); // ** 第二層路徑
    watch(['src/*.html', 'src/layout/*.html'], includeHTML).on('change', reload); // ** 第二層路徑
    watch('src/js/*.js', ugjs).on('change', reload);
    watch(['src/images/*.*', 'src/images/**/*.*'], moveimg).on('change', reload);
    watch('src/*.py', pyth).on('change', reload);
    watch('src/cofig/*.toml', pycog).on('change', reload); // ** 第二層路徑
    done();
}

exports.default = series(parallel(includeHTML, sassstyle, ugjs, moveimg,pyth,pycog), browser);


//清除舊檔案
const clean = require('gulp-clean');

function clear() {
    return src('dist', { read: false, allowEmpty: true })//不去讀檔案結構，增加刪除效率  / allowEmpty : 允許刪除空的檔案
        .pipe(clean({ force: true })); //強制刪除檔案 
}

exports.clearall = clear;

//上線打包
exports.packages = series(clear, parallel(includeHTML, sassstyle, ugjs), imgmin ,moveimg,pyth,pycog);