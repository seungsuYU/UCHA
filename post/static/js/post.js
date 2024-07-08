document.addEventListener("DOMContentLoaded", function () {
    // 모달 열기 및 닫기
    var modal = document.getElementById("myModal");
    var searchModal = document.getElementById("searchModal");
    var openModalBtn = document.getElementById("openModal");
    var searchBtn = document.getElementById("search");
    var closeBtn = document.getElementsByClassName("close")[0];
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
  
    // 게시글 섹션을 JavaScript로 동적으로 추가
    var posts = [
      {
        id: 1,
        title: "게시글 제목 1",
        content: "게시글 내용 1",
      },
      {
        id: 2,
        title: "게시글 제목 2",
        content: "게시글 내용 2",
      },
      {
        id: 3,
        title: "게시글 제목 3",
        content: "게시글 내용 3",
      },
    ];
  
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

 // jquery 부분
 $('.modal_main_section')
 .on("dragover", dragover)
 .on("dragleave", dragleave)
 .on("drop", uploadFiles);

 function dragover(e) {
  e.stopPropagation();
  e.preventDefault();

  if (e.type == "dragover") {
    $(e.target).css({
      "background-color":"black",
      "outline-offset": "-20px"
    });
  }else {
    $(e.target).css({
      "background-color":"white",
      "outline-offset": "-10px"
    });
  }
 }

 function uploadFiles(e) {
  e.stopPropagation();
  e.preventDefault();

  e.dataTransfer = e.originalEvent.dataTransfer; 
  var files =  e.dataTransfer.files;

  if (files.length > 1) {
      alert('하나만 올려라.');
      return;
  }

  if (files[0].type.match(/image.*/)) {
      $(e.target).css({
          "background-image": "url(" + window.URL.createObjectURL(files[0]) + ")",
          "outline": "none",
          "background-size": "100% 100%"});
  }else{
      alert('이미지가 아닙니다.');
      return;
  }

}
