// 사용자가 이미지 파일을 등록하면 이미지 속성으로 값을 가져온다. 
// case 1
let imgElement = document.getElementById('imageSrc');
let inputElement = document.getElementById('imgInput');
inputElement.addEventListener('change', (e) => {
    imgElement.src = URL.createObjectURL(e.target.files[0]);
}, false);

// window + shift + s로 이미지 캡쳐 -> ctrlv 로 복붙
// case 2
window.addEventListener("paste", function(e) {
    let item = Array.from(e.clipboardData.items).find(x => /^image\//.test(x.type));
    let blob = item.getAsFile();

    imgElement.src = URL.createObjectURL(blob);
})

// 파일 올리면 이미지 경로 획득 -> 이미지가 로드 되면
imgElement.addEventListener('load', imgRec);
// imgElement.addEventListener('change', imgRec);
function imgRec() {
    
    // 이미지 읽어오기
    let image = cv.imread(imgElement);
    cv.imshow('canvas', image);

    // 원본 이미지를 복사해둔다. copy() -> clone()
    let original = image.clone();
    // cv.imshow('canvas2', original); //grayscale로 변환

    // grayscale로 변환한다.
    let gray = new cv.Mat();
    cv.cvtColor(image, gray, cv.COLOR_BGR2GRAY, 0);
    // cv.imshow('gray', gray); 
    
    // 적절한 kernal을 적용해 Blur 처리를 한다.
    let blur = new cv.Mat();
    let ksize = new cv.Size(3, 3);
    cv.GaussianBlur(gray, blur, ksize, 0, 0, cv.BORDER_DEFAULT)
    // cv.imshow('blur', blur) 
    
    //바이너리 이미지를 생성한다.
    let threshINV = new cv.Mat();
    cv.threshold(blur, threshINV, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU);
    // cv.imshow('threshold', threshINV) 
    
    
    /** 
    바이너리 이미지에 vertical 커널 적용
    cv2.getStructuringElement(cv2.MORPH_RECT, (1,50)) -> cv.Mat.ones()로 대체하였음.    
    */
    /**
    * image opening params
    * src	source image. The number of channels can be arbitrary. The depth should be one of cv.CV_8U, cv.CV_16U, cv.CV_16S, cv.CV_32F or cv.CV_64F
    * dst	destination image of the same size and type as source image.
    * op	type of a morphological operation, (see cv.MorphTypes).
    * kernel	structuring element. It can be created using cv.getStructuringElement.
    * anchor	anchor position with the kernel. Negative values mean that the anchor is at the kernel center.
    * iterations	number of times dilation is applied.
    * borderType	pixel extrapolation method(see cv.BorderTypes).
    * borderValue	border value in case of a constant border. The default value has a special meaning.
    */
    let vertikernel = cv.Mat.ones(1, 50, cv.CV_8U);
    let openedINV = new cv.Mat();
    let anchor = new cv.Point(-1, -1);
    cv.morphologyEx(threshINV, openedINV, cv.MORPH_OPEN, vertikernel, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());

    // horizental 커널 적용
    let horikerner = cv.Mat.ones(50, 1, cv.CV_8U)
    let opened2INV = new cv.Mat();
    cv.morphologyEx(openedINV, opened2INV, cv.MORPH_OPEN, horikerner, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());

    // cv.imshow('kernal', opened2INV); 윤곽선 검출
    let contours = new cv.MatVector();
    let hierarchy = new cv.Mat();
    let openedINV_clone = opened2INV.clone();
    cv.findContours(openedINV_clone, contours, hierarchy, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE);
    
    let cnt = contours.get(0);
    let rect = cv.boundingRect(cnt);
   
    // console.log("rect.x : " + rect.x);
    // console.log("rect.y : " + rect.y);
    // console.log("rect.width: " + rect.width)
    // console.log("rect.height: " + rect.height)

    let crop = new cv.Mat();
    let rectangle = new cv.Rect(rect.x, rect.y, rect.width, rect.height);
    crop = original.roi(rectangle);

    // cv.imshow('crop', crop);
    
    makeInitalBoard(crop);
    console.log(board);

    crop.delete();
    contours.delete();
    hierarchy.delete();
    cnt.delete();
    openedINV_clone.delete();
    openedINV.delete();
    opened2INV.delete();
    threshINV.delete();
    blur.delete();
    gray.delete();
    image.delete();
    original.delete();
};

var setStoneCnt = 0;
var beforecell;
function setStoneOnBoard(isInterrupt, idText) {
    let text = idText.match(/\d{1}_\d{1}/)[0].split('_');
    let x = text[0] - 1 ;
    let y = text[1] - 1 ;

    if(isInterrupt == true){
        board[x][y] = -1 // 방해물
        let interImg = document.createElement("img");
        interImg.src = '../images/block/interrupt.png';
        interImg.style.width="75px";
        interImg.style.height="75px";
        let cell = document.getElementById(idText);
        cell.appendChild(interImg);
        cell.classList.replace('empty_cell', "fill_cell");
    }
    else {
        // 넣을 이미지 정보 입력
        let slimeImg = document.createElement("img");
        let pinkbinImg = document.createElement("img");

        pinkbinImg.src = '../images/block/pinkbin.png';
        slimeImg.src = '../images/block/slime.png';

        pinkbinImg.style.width="75px";
        pinkbinImg.style.height="75px";
        slimeImg.style.width="75px";
        slimeImg.style.height="75px";
        // 배열 인덱스 정보 추출
        
        
        let cell = document.getElementById(idText);
        console.log(cell.classList);    
        if(cell.classList[0] == 'empty_cell'){
            if(setStoneCnt % 2 == 0) {
                board[x][y] = 1; // 핑크빈
                cell.appendChild(pinkbinImg);
                
            }
            else{
                board[x][y] = 2; // 슬라임
                cell.appendChild(slimeImg);
            }
            cell.classList.replace('empty_cell', "fill_cell");
            setStoneCnt ++;
        }
        else{
            console.log("cell id is: ", cell.classList[0]);
        }

        beforecell = document.getElementById('cell'+(x+1)+'_'+(y+1)); 
    }
}
// 되돌리기 기능
// 일단 한번만 되돌리기 가능하게끔.
// 오류 버튼을 두번 눌러야만 실행이 된다..?
$(document).on("click","#revertBtn",()=>{
    beforecell.removeChild(beforecell.childNodes[2]);
    console.log("되돌리기 완료.");
    beforecell.classList.replace("fill_cell", "empty_cell");
    console.log(beforecell.childNodes);
    // 돌 개수 카운트를 1 줄이고
    setStoneCnt -= 1;   
});
     

var board;
function reloadPage() {
    location.reload();
}
function makeInitalBoard(image) {    
    
    // ES2015 이후 이러한 방식으로 배열만드는 것을 지원한다고 함. 8*8 배열 생성
    board = Array.from(Array(8), () => new Array(8));
    
    // 방해물 위치를 기록해두는 5*2 배열 생성성
    var interrupt = Array.from(Array(5), ()=> new Array(2)); 
    for (var x = 0; x < 8; x++)
        for (var y = 0; y < 8; y++)
            board[x][y] = 0;
    
    board[3][3] = 1;
    board[3][4] = 2;
    board[4][3] = 2;
    board[4][4] = 1;
    

    let height = image.cols;
    let width = image.rows;
    let cellHeight = height / 8;
    let cellWidth = width / 8;
    
    let gray = new cv.Mat();
    cv.cvtColor(image, gray, cv.COLOR_BGR2GRAY, 0);
    let blur = new cv.Mat();
    let ksize = new cv.Size(3, 3);
    cv.GaussianBlur(gray, blur, ksize, 0, 0, cv.BORDER_DEFAULT)

    let inter_cnt = 0;
    for(var x = cellWidth / 2; x < width; x += cellWidth) {
        for(var y = cellHeight / 2; y < height; y+= cellHeight) {
            let gray = blur.ucharPtr(x, y)[0];            
            console.log("gray is : ", gray);

            let xIndex = parseInt(x / cellWidth);
            let yIndex = parseInt(y / cellHeight);
            if(gray <= 60) {
                board[xIndex][yIndex] = -1;
                interrupt[inter_cnt][0] = xIndex + 1; // id는 1부터 시작하고 
                interrupt[inter_cnt++][1] = yIndex + 1; // 배열은 0부터 인덱스시작이니까
            }

        }
    }    

    // 방해물 추가
    for(var x = 0; x < 5; x++ ) {
        let idText = "cell"+interrupt[x][0]+"_"+interrupt[x][1];
        setStoneOnBoard(true, idText);
    }
    
    setStoneOnBoard(false, 'cell4_4');    
    setStoneOnBoard(false, 'cell5_4');
    setStoneOnBoard(false, 'cell5_5');
    setStoneOnBoard(false, 'cell4_5');
}
function clickBoard() { 
    
    console.log(event.target);
    console.log(event.target.id);
    setStoneOnBoard(false, event.target.id);
   
}

