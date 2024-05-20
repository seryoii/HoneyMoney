<template>
  <v-container>
    <v-container class="map-component-under">
      <v-row>
        <v-col>
          <v-btn class="button-custom" @click="searchOnMap">검색하기</v-btn>
        </v-col>
        <v-col>
          <v-btn class="button-custom" @click="searchNearbyBanks">현 위치 주변 검색</v-btn>
        </v-col>
      </v-row>
      <!-- 지도를 표시할 컨테이너 -->
      <v-container id="mapContainer" class="map-container"></v-container>
    </v-container>
  </v-container>
</template>
<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

// props 정의
const props = defineProps({
  province: String,
  city: String,
  bank: String,
});

const map = ref(null);
const infowindow = ref(null);
const markers = ref([]); // 마커를 저장할 배열 추가
const searchKeyword = ref(""); // 검색어를 저장할 변수 추가

const loadKakaoMap = function () {
  // Kakao 지도 API 스크립트 동적으로 추가
  const script = document.createElement("script");
  const KAKAO_KEY = import.meta.env.VITE_KAKAO_MAP_API; // APP KEY
  script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${KAKAO_KEY}&autoload=false&libraries=services`;
  script.async = true;
  script.onload = () => {
    // Kakao 지도 API 로드 완료 후 실행할 콜백 함수
    window.kakao.maps.load(function () {
      initializeKakaoMap();
    });
  };

  document.head.appendChild(script);
};

const initializeKakaoMap = function () {
  let lat = 36.10706;
  let lon = 128.415494;
  if (navigator.geolocation) {
    // GeoLocation을 이용해서 접속 위치를 얻어옵니다
    navigator.geolocation.getCurrentPosition(function (position) {
      lat = position.coords.latitude; // 위도
      lon = position.coords.longitude; // 경도

      // Kakao 지도 API 초기화
      console.log("Initializing Kakao Map");
      const mapContainer = document.getElementById("mapContainer");
      const mapOption = {
        center: new window.kakao.maps.LatLng(lat, lon),
        level: 3,
      };

      map.value = new window.kakao.maps.Map(mapContainer, mapOption);
      infowindow.value = new window.kakao.maps.InfoWindow({ zIndex: 1 });

      // 현재 위치 기준 은행 검색
      searchPlacesByCoordinates(lat, lon);
    });
  } else {
    console.log("Geolocation을 사용할 수 없습니다.");
  }
};

const handleWindowResize = function () {
  // 창 크기가 변경될 때 지도 크기 업데이트
  if (map.value) {
    map.value.relayout();
  }
};

onMounted(() => {
  // Kakao 지도 API 스크립트 동적으로 추가
  loadKakaoMap();
  // 창 크기가 변경될 때의 이벤트 리스너 추가
  window.addEventListener("resize", handleWindowResize);
});

onBeforeUnmount(() => {
  // 컴포넌트가 파괴될 때 이벤트 리스너 제거
  window.removeEventListener("resize", handleWindowResize);
});

const searchOnMap = function () {
  console.log("Button clicked");
  searchKeyword.value = `${props.province} ${props.city} ${props.bank}`;
  console.log("Search Keyword:", searchKeyword.value);
  searchPlaces(searchKeyword.value);
  console.log(props.bank);
  // 상품 검색 함수 실행
};

const searchNearbyBanks = function () {
  if (map.value) {
    const center = map.value.getCenter();
    searchPlacesByCoordinates(center.getLat(), center.getLng());
  } else {
    alert("지도가 초기화되지 않았습니다.");
  }
};

const searchPlacesByCoordinates = function (lat, lon) {
  const ps = new window.kakao.maps.services.Places();
  const callback = function (data, status, pagination) {
    if (status === window.kakao.maps.services.Status.OK) {
      // 검색 결과가 OK일 때 기존 마커들을 모두 제거
      removeAllMarkers();

      // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
      // LatLngBounds 객체에 좌표를 추가
      let bounds = new window.kakao.maps.LatLngBounds();

      for (let i = 0; i < data.length; i++) {
        displayMarker(data[i]);
        bounds.extend(new window.kakao.maps.LatLng(data[i].y, data[i].x));
      }
      // 검색된 장소 위치를 기준으로 지도 범위를 재설정
      map.value.setBounds(bounds);
      // 이전에 열린 인포윈도우 닫기
      infowindow.value.close();
    } else {
      alert("현재 위치 주변에 해당 은행이 없습니다.");
    }
  };

  // 현재 위치 기준으로 반경 1000m 내에 있는 은행 검색
  ps.keywordSearch("은행", callback, {
    location: new window.kakao.maps.LatLng(lat, lon),
    radius: 1000,
  });
};

const searchPlaces = function (keyword) {
  const ps = new window.kakao.maps.services.Places();

  ps.keywordSearch(keyword, placesSearchCB);
};

const placesSearchCB = function (data, status, pagination) {
  if (status === window.kakao.maps.services.Status.OK) {
    // 검색 결과가 OK일 때 기존 마커들을 모두 제거
    removeAllMarkers();

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
    // LatLngBounds 객체에 좌표를 추가
    let bounds = new window.kakao.maps.LatLngBounds();

    for (let i = 0; i < data.length; i++) {
      displayMarker(data[i]);
      bounds.extend(new window.kakao.maps.LatLng(data[i].y, data[i].x));
    }
    // 검색된 장소 위치를 기준으로 지도 범위를 재설정
    map.value.setBounds(bounds);
    // 이전에 열린 인포윈도우 닫기
    infowindow.value.close();
  } else {
    alert("선택한 지역에 해당 은행이 없습니다. 다른 은행을 선택해주세요.");
  }
};

const displayMarker = function (place) {
  const marker = new window.kakao.maps.Marker({
    map: map.value,
    position: new window.kakao.maps.LatLng(place.y, place.x),
  });

  window.kakao.maps.event.addListener(marker, "click", () => {
    infowindow.value.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + "</div>");
    infowindow.value.open(map.value, marker);
  });

  // 생성된 마커를 배열에 추가
  markers.value.push(marker);
};

const removeAllMarkers = function () {
  // 배열에 저장된 모든 마커를 제거
  for (let i = 0; i < markers.value.length; i++) {
    markers.value[i].setMap(null);
  }
  // 배열 비우기
  markers.value = [];
};

const searchProducts = function (params) {};
</script>

<style scoped>
.map-component-under {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.map-search-btn {
  width: fit-content;
}
.map-container {
  width: 100%;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: auto;
  margin-right: auto;
  height: 500px;
}
.button-custom {
  color: #916415;
  font-weight: bold;
  background-color: #fef5e7;
}
</style>
