$(function() {
  $(".typed").typed({
    strings: [
      "systemclt status Abhishek<br/>" + 
      "><span class='caret'>$</span> skills: networking [mpls,TCP/IP,BGP,routing protocols,STP,Vlans]<br/> ^100" +
      "><span class='caret'>$</span> -----[+]netw <a href='http://www.googh</a><br/> ^100" +
      "><span class='caret'>$</span> hobbies: badminton,singing <br/>" +
      ],
    showCursor: true,
    cursorChar: '_',
    autoInsertCss: true,
    typeSpeed: 0.001,
    startDelay: 50,
    loop: false,
    showCursor: false,
    onStart: $('.message form').hide(),
    onStop: $('.message form').show(),
    onTypingResumed: $('.message form').hide(),
    onTypingPaused: $('.message form').show(),
    onComplete: $('.message form').show(),
    onStringTyped: function(pos, self) {$('.message form').show();},
  });
  $('.message form').hide()
});
