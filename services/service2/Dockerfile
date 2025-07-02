FROM ghcr.io/openfaas/of-watchdog:latest AS watchdog
FROM python:3.11.9

COPY --from=watchdog /fwatchdog /usr/local/bin/fwatchdog
RUN chmod +x /usr/local/bin/fwatchdog

RUN pip install --no-cache-dir requests

WORKDIR /function
COPY entrypoint.py . 

RUN addgroup --system func && adduser --system --ingroup func func
USER func

ENV fprocess="python3 entrypoint.py" \
    mode="streaming" \
    SERVICE1_URL="http://service1:8080/"

EXPOSE 8080
CMD ["/usr/local/bin/fwatchdog"]
