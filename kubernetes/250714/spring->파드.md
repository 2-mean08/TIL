저의 이전 답변이 복사/붙여넣기 시 원하시는 마크다운 형식으로 제대로 동작하지 않아 죄송합니다. 마크다운 에디터나 플랫폼에 따라 렌더링 방식이 다를 수 있기 때문에 발생할 수 있는 문제입니다.

이번에는 **마크다운 코드 블록과 적절한 줄 바꿈을 명확히 사용하여, 일반 텍스트 편집기에 붙여넣으셔도 마크다운 형식 그대로 인식될 수 있도록 재작성**했습니다. 아래 내용을 복사하여 마크다운을 지원하는 에디터(예: VS Code, Typora, GitHub 등)에 붙여넣어 보시면 원하시는 형태로 나타날 것입니다.

-----

# 쿠버네티스(Kubernetes) 기본 개념 및 Spring Boot 앱 배포

-----

## 쿠버네티스란?

**쿠버네티스**는 다수의 컨테이너를 효율적으로 배포, 확장 및 관리하기 위한 오픈 소스 시스템입니다.

-----

## 파드(Pod)란?

**파드**는 쿠버네티스에서 **하나의 프로그램을 실행시키는 단위**입니다. 파드는 하나 이상의 컨테이너 그룹, 스토리지 자원, 고유한 네트워크 IP, 그리고 컨테이너를 실행하는 방법을 제어하는 옵션으로 구성됩니다.

### 파드에 접속하는 방법

* **포트 포워딩(Port Forwarding)**

  ```bash
  kubectl port-forward pod/[파드명] [포트번호]
  ```

    * `[포트번호]` 자리에 `[로컬포트번호]:[파드포트번호]`를 지정하면 `localhost:[로컬포트번호]`로 접속할 수 있습니다.
    * 예시: `kubectl port-forward pod/my-spring-pod 8080:8013` (로컬 8080 포트로 파드의 8013 포트에 접속)

* **내부에 접속하기 (Shell 접속)**

  ```bash
  kubectl exec -it [파드명] -- bash
  ```

    * 예시: `kubectl exec -it spring-pod -- bash`
    * 접속 후 나가려면 `exit`를 입력합니다.

-----

## Spring Boot 서버를 파드로 띄우는 과정

### 1\. Spring Boot 애플리케이션 (Hello, World 컨트롤러)

`AppController.java`

```java
package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AppController{
 @GetMapping("/")
 public String home() {
  return "Hello, World";
 }
}
```

### 2\. Docker 이미지 생성 설정 파일 (Dockerfile)

Spring Boot 빌드 결과물인 `.jar` 파일을 도커 이미지로 만들기 위한 설정입니다.

`Dockerfile`

```dockerfile
FROM openjdk:17-jdk

COPY build/libs/*SNAPSHOT.jar app.jar

ENTRYPOINT ["java", "-jar", "/app.jar"]
```

### 3\. Spring Boot 프로젝트 빌드

터미널에서 다음 명령어를 실행하여 `.jar` 파일들을 생성합니다.

```bash
gradle clean build
```

이 명령어를 실행하면 `build/libs/` 디렉터리에 `.jar` 파일이 생성됩니다.

### 4\. Docker 이미지 빌드

`Dockerfile`이 있는 경로에서 다음 명령어를 실행하여 도커 이미지를 생성합니다. **Docker Desktop이 실행 중이어야 합니다.**

```bash
docker build -t spring-server .
```

생성된 도커 이미지 목록을 확인하려면 다음 명령어를 사용합니다.

```bash
docker image ls
```

### 5\. 쿠버네티스 YAML 파일 생성 (Manifest)

파드를 정의하는 YAML 파일입니다.

`spring-pod.yaml`

```yaml
apiVersion: v1
kind: Pod

metadata:
  name: spring-pod

spec:
  containers:
    - name: spring-container
      image: spring-server
      ports:
        - containerPort: 8013
      imagePullPolicy: IfNotPresent
```

### 6\. 파드 생성 및 삭제 명령어

* **파드 생성:**

  ```bash
  kubectl apply -f spring-pod.yaml
  ```

* **파드 삭제:**

  ```bash
  kubectl delete pod [파드명]
  ```

  예시: `kubectl delete pod spring-pod`

-----

## 이미지 풀 정책(Image Pull Policy)

YAML 파일을 읽어 파드를 생성할 때, 이미지를 어떻게 가져올지에 대한 정책입니다.

* **`IfNotPresent`**: 노드에 이미지가 없을 때만 레지스트리에서 이미지를 가져옵니다. 이미 있다면 다시 가져오지 않습니다.
* **`Always`**: 파드가 생성될 때마다 항상 레지스트리에서 이미지를 가져옵니다. (단, 동일한 digest면 캐시를 사용합니다.)
* **`Never`**: 절대 이미지를 가져오지 않습니다. 노드에 이미지가 없으면 컨테이너가 실행되지 않습니다.

-----
