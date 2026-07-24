# Page Pulse
# Live Demo

Frontend:
https://page-pulse-vj8z.vercel.app

Backend API:
https://page-pulse-uajo.onrender.com

API Documentation:
https://page-pulse-uajo.onrender.com/docs
Production-grade URL auditing service designed to analyze website performance, availability, and metadata while providing scalable, reliable, and maintainable infrastructure.

Page Pulse performs automated website audits with support for:

- URL validation
- HTTP status monitoring
- Response time measurement
- Page metadata extraction
- HTTPS verification
- Result caching
- Rate limiting
- Structured logging
- Automated testing and CI


# Features

## Audit Service

The service analyzes URLs and provides:

- HTTP response status
- Website response time
- HTML title extraction
- HTTPS availability check
- Audit result caching


## Reliability and Performance

Implemented production features:

- Request timeout handling
- Async HTTP requests
- Concurrency control
- Configurable caching using TTL
- Structured error responses
- Rate limiting per client


## Testing and CI

The project includes:

- Automated test suite
- Pytest integration
- GitHub Actions CI pipeline
- Automated verification on every push


# System Architecture

The service follows a scalable architecture separating request handling from audit processing.


```
Client

   |

Load Balancer

   |

FastAPI Application

   |

Rate Limiter

   |

Audit Service

   |

Redis Cache

   |

Database
```


Detailed architecture documentation:

```
docs/architecture.md
```


# API Documentation


## Health Check


### Endpoint

```
GET /
```


### Response

```json
{
  "message": "Page Pulse API is running"
}
```


---

# URL Audit


## Endpoint

```
POST /audit
```


## Request Body

```json
{
  "url": "https://example.com"
}
```


## Successful Response

```json
{
  "url": "https://example.com/",
  "status": 200,
  "response_time_ms": 213.05,
  "title": "Example Domain",
  "https": true,
  "cached": false
}
```


## Cached Response

Repeated requests for the same URL within the configured cache duration return cached results.

Example:

```json
{
  "url": "https://example.com/",
  "cached": true
}
```


## Error Response

All errors follow a structured format:

```json
{
  "error": "Invalid URL",
  "request_id": "abc123"
}
```


# Configuration


## Cache Configuration

Cache duration can be configured using:

```
CACHE_TTL=300
```

Value is specified in seconds.

Default:

```
300 seconds
```


## Rate Limiting Configuration

Example:

```
RATE_LIMIT=10
RATE_WINDOW=60
```

This allows 10 requests per client within a 60 second window.


# Local Development


## Clone Repository

```bash
git clone https://github.com/HarshithaTentu/page-pulse.git
```


## Create Virtual Environment

```bash
python -m venv .venv
```


## Activate Environment


Mac/Linux:

```bash
source .venv/bin/activate
```


## Install Dependencies

```bash
pip install -r requirements.txt
```


## Run Application

```bash
uvicorn app.main:app --reload
```


Application will be available at:

```
http://127.0.0.1:8000
```


API documentation:

```
http://127.0.0.1:8000/docs
```


# Running Tests


Execute:

```bash
pytest
```


Expected output:

```
4 passed
```


# Continuous Integration


GitHub Actions automatically executes tests on every push.

Pipeline:

```
Code Push

   |

Install Dependencies

   |

Run Test Suite

   |

Build Verification
```


# Project Structure


```
page-pulse/

├── app/
│   ├── main.py
│   ├── services.py
│   ├── cache.py
│   ├── schemas.py
│   └── middleware.py
│
├── tests/
│
├── docs/
│   ├── architecture.md
│   ├── technology-decisions.md
│   ├── failure-analysis.md
│   └── operations-plan.md
│
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
```


# Production Architecture Documentation


Additional design documents:

## Architecture

```
docs/architecture.md
```

Contains:

- System components
- Data flow
- Scaling strategy
- State management


## Technology Decisions

```
docs/technology-decisions.md
```

Contains:

- Technology selection reasoning
- Alternative evaluation
- Trade-off analysis


## Failure Analysis

```
docs/failure-analysis.md
```

Contains:

- Production failure scenarios
- Impact analysis
- Mitigation strategies


## Operations Plan

```
docs/operations-plan.md
```

Contains:

- Monitoring strategy
- Alerting
- Deployment process
- Rollback procedure


# Deployment

The service is designed for cloud deployment with:

- Containerized API services
- Redis caching layer
- PostgreSQL persistence layer
- Horizontal scaling support
- Automated deployment pipelines


# License

This project was developed as part of the Digital Heroes Training Task.
