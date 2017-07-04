module.exports = function (grunt) {

    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        uglify: {
            js: {
                options: {
                    sourceMap: true,
                    sourceMapName: 'flipper.min.js.map'
                },
                files: {
                    'flipper.min.js': ['src/flipper.js']
                }
            }
        }
    });

    grunt.registerTask('default',[
        'uglify:js'
    ]);

};
