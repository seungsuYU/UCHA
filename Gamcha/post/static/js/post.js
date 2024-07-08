document.addEventListener("DOMContentLoaded", function () {
    // 모달 열기 및 닫기
    var modal = document.getElementById("myModal");
    var searchModal = document.getElementById("searchModal");
    var openModalBtn = document.getElementById("openModal");
    var searchBtn = document.getElementById("search");
    var closeBtn = document.getElementById("close");
    var searchInput = document.getElementById("searchInput");
  
    openModalBtn.onclick = function () {
      modal.style.display = "flex";
      modal.style.alignContent = 'center';
      modal.style.justifyContent = 'center';
    };
  
    closeBtn.onclick = function () {
      modal.style.display = "none";
    };
  
    searchBtn.onclick = function () {
      searchModal.style.display = "flex";
      searchInput.focus();
    };
  
    window.onclick = function (event) {
      if (event.target == modal) {
        modal.style.display = "none";
      } else if (event.target == searchModal) {
        searchModal.style.display = "none";
      }
    };
  
      
    var rightSections = document.querySelector(".right__sections");
  
    posts.forEach(function (post) {
      var listItem = document.createElement("li");
      var title = document.createElement("h3");
      var content = document.createElement("p");
  
      title.textContent = post.title;
      content.textContent = post.content;
  
      listItem.appendChild(title);
      listItem.appendChild(content);
      rightSections.appendChild(listItem);
    });
  });
  
  // 커뮤니티 a태그 클릭시 이벤트 발생
  function contents__section() {
  alert('개발중 입니다.')
  }

  // 작성 버튼 클릭 시 AJAX요청
// post.js 수정된 버전

// post.js

document.addEventListener('DOMContentLoaded', function() {
  const yesPostButton = document.getElementById('yes__post');

  if (yesPostButton) {
      yesPostButton.addEventListener('click', function() {
          const title = document.querySelector('.right__header__coment input').value;
          const content = document.querySelector('.right__main__text textarea').value;

          // CSRF 토큰 가져오기
          const csrftoken = getCookie('csrftoken');

          // AJAX 요청 보내기
          const xhr = new XMLHttpRequest();
          xhr.open('POST', '/post/create/', true);
          xhr.setRequestHeader('Content-Type', 'application/json');
          xhr.setRequestHeader('X-CSRFToken', csrftoken); // CSRF 토큰 설정
          xhr.onreadystatechange = function() {
              if (xhr.readyState === XMLHttpRequest.DONE) {
                  if (xhr.status === 200) {
                      // 성공적으로 게시글이 등록되었을 때 처리
                      alert('게시글이 등록되었습니다.');
                      // 원하는 추가 작업 수행
                  } else {
                      // 오류 처리
                      alert('게시글 등록에 실패했습니다.');
                  }
              }
          };
          const data = JSON.stringify({ title: title, content: content });
          xhr.send(data);
      });
  }
});

// CSRF 토큰을 가져오는 함수
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const xhr = new XMLHttpRequest();
xhr.open('POST', '/post/create/', true);

 // jquery 부분
//  드래그 앤 드롭 못함