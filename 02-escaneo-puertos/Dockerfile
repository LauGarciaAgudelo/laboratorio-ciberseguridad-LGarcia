
FROM alpine:3.21

RUN apk add --no-cache netcat-openbsd python3 bind-tools

WORKDIR /app

COPY entrypoint.sh /app/entrypoint.sh

RUN sed -i 's/\r$//' /app/entrypoint.sh \
    && chmod +x /app/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]
