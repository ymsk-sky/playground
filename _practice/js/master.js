var app = new Vue({
  el: '#app',
  data: {
    imgSrc: "img/w.png",
    isSelected: false
  },
  methods: {
    changeImg: function(e) {
      _id = e.target.id
      if (_id == 'a-img') {
        this.imgSrc = 'img/char_a.png'
      }
      else if (_id == 'b-img') {
        this.imgSrc = 'img/char_b.png'
      }
      else if (_id == 'c-img') {
        this.imgSrc = 'img/char_c.png'
      }
    },
    stopAnime: function() {
      this.isSelected = false
    }
  },
  watch: {
    imgSrc: function() {
      this.isSelected = true
    }
  }
})
