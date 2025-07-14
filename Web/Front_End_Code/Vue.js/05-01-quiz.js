var app = new Vue({
    el: '#app',
    data : {
        message: 'Hello Vue.js',
        name: 'James',
        uid: 10,
        flag: true
    },
    methods: {
        clickBtn() {
            console.log('hi');
        },
        touch() {
            this.uid += 1
        }
    }
});