## 1. Отдача статического документа напрямую через Nginx
- **Server Software**: nginx/1.27.3
- **Server Hostname**: localhost
- **Server Port**: 80
- **Document Path**: /static/main/img/Iam.jpg
- **Document Length**: 7634880 bytes
### Результаты:
- Concurrency Level: 10  
- Time taken for tests: 0.600 seconds  
- Complete requests: 1000  
- Failed requests: 0  
- Total transferred: 4400486000 bytes  
- HTML transferred: 4400140000 bytes  
- Requests per second: 1666.67 #/sec (mean)  
- Time per request: 6.000 ms (mean)  
- Transfer rate: 7333333.33 Kbytes/sec received
### Connection Times (ms)
| Connect | Processing | Waiting | Total |
|---------|------------|---------|-------|
| 0       | 6          | 0       | 6     |
### Percentage of requests served within a certain time (ms)
| Time (ms) | Percentage |
|-----------|------------|
| 50%       | 6          |
| 66%       | 6          |
| 75%       | 6          |
| 80%       | 7          |
| 90%       | 7          |
| 95%       | 8          |
| 98%       | 8          |
| 99%       | 9          |
| 100%      | 9          |
---
## 2. Отдача статического документа напрямую через Gunicorn
- **Server Software**: gunicorn
- **Server Hostname**: localhost
- **Server Port**: 8000
- **Document Path**: /static/main/img/Iam.jpg
- **Document Length**: 7634880 bytes
### Результаты:
- Concurrency Level: 10  
- Time taken for tests: 0.650 seconds  
- Complete requests: 1000  
- Failed requests: 0  
- Total transferred: 4400505000 bytes  
- HTML transferred: 4400140000 bytes  
- Requests per second: 1538.46 #/sec (mean)  
- Time per request: 6.500 ms (mean)  
- Transfer rate: 6769230.77 Kbytes/sec received
### Connection Times (ms)
| Connect | Processing | Waiting | Total |
|---------|------------|---------|-------|
| 0       | 6          | 5       | 6     |
### Percentage of requests served within a certain time (ms)
| Time (ms) | Percentage |
|-----------|------------|
| 50%       | 6          |
| 66%       | 6          |
| 75%       | 7          |
| 80%       | 7          |
| 90%       | 8          |
| 95%       | 10         |
| 98%       | 12         |
| 99%       | 15         |
| 100%      | 18         |
---
## 3. Отдача динамического документа напрямую через Gunicorn
- **Server Software**: gunicorn
- **Server Hostname**: localhost
- **Server Port**: 8000
- **Document Path**: /question/3/
- **Document Length**: 7478 bytes
### Результаты:

- Concurrency Level: 10  
- Time taken for tests: 12.873 seconds  
- Complete requests: 1000  
- Failed requests: 0  
- Total transferred: 7678000 bytes  
- HTML transferred: 7382000 bytes  
- Requests per second: 77.77 #/sec (mean)  
- Time per request: 128.73 ms (mean)  
- Transfer rate: 596.43 Kbytes/sec received  

### Connection Times (ms)

| Connect | Processing | Waiting | Total |
|---------|------------|---------|-------|
| 0       | 128        | 128     | 128   |

### Percentage of requests served within a certain time (ms)

| Time (ms) | Percentage |
|-----------|------------|
| 50%       | 129        |
| 66%       | 130        |
| 75%       | 131        |
| 80%       | 132        |
| 90%       | 133        |
| 95%       | 134        |
| 98%       | 136        |
| 99%       | 138        |
| 100%      | 141        |

---

## 4. Отдача динамического документа через проксирование запроса с Nginx на Gunicorn

- Server Software: nginx/1.27.3  
- Server Hostname: localhost  
- Server Port: 80  
- Document Path: /question/3/  
- Document Length: 7478 bytes  

### Результаты:

- Concurrency Level: 10  
- Time taken for tests: 9.637 seconds  
- Complete requests: 1000  
- Failed requests: 0  
- Total transferred: 7691000 bytes  
- HTML transferred: 7382000 bytes  
- Requests per second: 103.76 #/sec (mean)  
- Time per request: 96.37 ms (mean)  
- Transfer rate: 793.00 Kbytes/sec received  

### Connection Times (ms)

| Connect | Processing | Waiting | Total |
|---------|------------|---------|-------|
| 0       | 96         | 96      | 96    |

### Percentage of requests served within a certain time (ms)

| Time (ms) | Percentage |
|-----------|------------|
| 50%       | 94         |
| 66%       | 96         |
| 75%       | 97         |
| 80%       | 98         |
| 90%       | 99         |
| 95%       | 100        |
| 98%       | 102        |
| 99%       | 105        |
| 100%      | 107        |

---

## 5. Отдача динамического документа через проксирование запроса с Nginx на Gunicorn с кэшированием на Nginx (Proxy Cache)

- Server Software: nginx/1.27.3  
- Server Hostname: localhost  
- Server Port: 80  
- Document Path: /question/3/  
- Document Length: 7478 bytes  

### Результаты:

- Concurrency Level: 10  
- Time taken for tests: 0.198 seconds  
- Complete requests: 1000  
- Failed requests: 0  
- Total transferred: 7691000 bytes  
- HTML transferred: 7382000 bytes  
- Requests per second: 5050.25 #/sec (mean)  
- Time per request: 0.198 ms (mean)  
- Transfer rate: 11346.34 Kbytes/sec received  

### Connection Times (ms)

| Connect | Processing | Waiting | Total |
|---------|------------|---------|-------|
| 0       | 1          | 1       | 1     |

### Percentage of requests served within a certain time (ms)

| Time (ms) | Percentage |
|-----------|------------|
| 50%       | 0          |
| 66%       | 0          |
| 75%       | 0          |
| 80%       | 0          |
| 90%       | 0          |
| 95%       | 0          |
| 98%       | 2          |
| 99%       | 22         |
| 100%      | 154        |