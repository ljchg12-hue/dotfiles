# Forensics Tools Configuration
<!-- Created: 2025-12-22 | For Claude Code Usage -->

## 📦 설치된 도구

### 1. Volatility3 (메모리 포렌식)
- **버전**: 2.26.2
- **명령어**: `vol`
- **위치**: `/home/leejc5147/.local/bin/vol`
- **설치**: pip3 (user)

**기본 사용법**:
```bash
# 플러그인 목록
vol --help

# Windows 메모리 덤프 분석
vol -f memory.dump windows.info
vol -f memory.dump windows.pslist
vol -f memory.dump windows.netscan
vol -f memory.dump windows.malfind

# Linux 메모리 덤프 분석
vol -f memory.dump linux.info
vol -f memory.dump linux.pslist

# 출력 저장
vol -f memory.dump windows.pslist -o /tmp/output.txt
```

**주요 플러그인**:
- `windows.info` - 시스템 정보
- `windows.pslist` - 프로세스 목록
- `windows.pstree` - 프로세스 트리
- `windows.netscan` - 네트워크 연결
- `windows.filescan` - 파일 스캔
- `windows.malfind` - 악성코드 탐지
- `windows.dlllist` - DLL 목록
- `windows.cmdline` - 커맨드라인 인자

### 2. Binwalk (펌웨어 분석)
- **버전**: 2.3.3
- **명령어**: `binwalk`
- **위치**: `/usr/bin/binwalk`
- **설치**: apt

**기본 사용법**:
```bash
# 파일 시그니처 스캔
binwalk firmware.bin

# 자동 추출
binwalk -e firmware.bin

# 상세 출력
binwalk -v firmware.bin

# Raw 검색
binwalk -R "\x1f\x8b\x08" firmware.bin

# Entropy 분석
binwalk -E firmware.bin
```

**주요 기능**:
- 파일 시그니처 탐지 (압축, 파일시스템, 실행파일 등)
- 자동 추출 (-e)
- Entropy 분석 (암호화 탐지)
- Raw 바이트 시퀀스 검색

### 3. Wireshark (GUI)
- **버전**: 4.2.2
- **명령어**: `wireshark`
- **위치**: `/usr/bin/wireshark`
- **설치**: apt

**사용법**:
```bash
# GUI 실행
wireshark capture.pcap

# 특정 인터페이스 캡처
wireshark -i eth0
```

**주의**: GUI 도구이므로 Claude가 직접 사용 불가. tshark 사용 권장.

### 4. tshark (CLI 네트워크 분석)
- **버전**: 4.2.2
- **명령어**: `tshark`
- **위치**: `/usr/bin/tshark`
- **설치**: apt

**기본 사용법**:
```bash
# PCAP 파일 읽기
tshark -r capture.pcap

# 필터링
tshark -r capture.pcap -Y "http"
tshark -r capture.pcap -Y "tcp.port == 80"
tshark -r capture.pcap -Y "ip.addr == 192.168.1.1"

# JSON 출력
tshark -r capture.pcap -T json > output.json

# 통계
tshark -r capture.pcap -z io,stat,1
tshark -r capture.pcap -z conv,tcp

# 특정 필드만 출력
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.port

# 라이브 캡처
tshark -i eth0 -w capture.pcap
```

**주요 필터**:
- `http` - HTTP 트래픽
- `tcp.port == 80` - 특정 포트
- `ip.addr == X.X.X.X` - 특정 IP
- `dns` - DNS 쿼리
- `tls.handshake` - TLS 핸드셰이크

---

## 🔧 Claude 사용 가이드

### PATH 설정
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Bash Tool 사용
Claude는 Bash tool을 통해 직접 명령어 실행 가능:

```python
# Volatility3 예시
Bash: vol -f /path/to/memory.dump windows.pslist

# Binwalk 예시
Bash: binwalk -e /path/to/firmware.bin

# tshark 예시
Bash: tshark -r /path/to/capture.pcap -Y "http" -T json
```

### 작업 흐름

**1. 메모리 분석**:
```
1. vol -f memory.dump windows.info  # 시스템 정보 확인
2. vol -f memory.dump windows.pslist  # 프로세스 목록
3. vol -f memory.dump windows.netscan  # 네트워크 연결
4. vol -f memory.dump windows.malfind  # 악성코드 탐지
```

**2. 펌웨어 분석**:
```
1. binwalk firmware.bin  # 시그니처 스캔
2. binwalk -E firmware.bin  # Entropy 확인
3. binwalk -e firmware.bin  # 자동 추출
4. ls -la _firmware.bin.extracted/  # 추출된 파일 확인
```

**3. 네트워크 분석**:
```
1. tshark -r capture.pcap  # 전체 패킷 확인
2. tshark -r capture.pcap -z io,stat,1  # 통계
3. tshark -r capture.pcap -Y "http"  # HTTP 필터
4. tshark -r capture.pcap -T json > analysis.json  # JSON 저장
```

---

## 📚 추가 리소스

### Volatility3
- GitHub: https://github.com/volatilityfoundation/volatility3
- 문서: https://volatility3.readthedocs.io/

### Binwalk
- GitHub: https://github.com/ReFirmLabs/binwalk
- Wiki: https://github.com/ReFirmLabs/binwalk/wiki

### Wireshark/tshark
- 공식 사이트: https://www.wireshark.org/
- 필터 참조: https://wiki.wireshark.org/DisplayFilters

---

## ⚠️ 주의사항

1. **메모리 덤프**: Volatility3는 대용량 파일 처리 시 시간이 오래 걸릴 수 있음
2. **Binwalk 추출**: `-e` 옵션은 현재 디렉토리에 파일 생성하므로 작업 디렉토리 주의
3. **tshark 권한**: 패킷 캡처 시 sudo 권한 필요할 수 있음
4. **출력 크기**: 대용량 PCAP 분석 시 출력이 매우 클 수 있으므로 필터 사용 권장

---

**버전**: 1.0
**작성일**: 2025-12-22
**적용 대상**: Claude Code (전역)
