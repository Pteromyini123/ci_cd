FROM ghcr.io/openfaas/of-watchdog:latest AS watchdog
FROM python:3.11.9


COPY --from=watchdog /fwatchdog /usr/local/bin/fwatchdog
RUN chmod +x /usr/local/bin/fwatchdog 

WORKDIR /function
COPY entrypoint.py . 

RUN addgroup --system func && adduser --system --ingroup func func
USER func

ENV fprocess="python3 entrypoint.py"
ENV mode="streaming"

EXPOSE 8080
CMD [ "fwatchdog" ]
