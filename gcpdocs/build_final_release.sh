#!/bin/bash
# Rebuild all four corpus archives from the final static docs/ tree, integrity-check each.
# Run only when no crawlers are writing to docs/. Sequential (2-CPU box).
set -e
cd /data/opencode/gcpdocs
rm -f releases/*.tar.gz
mkdir -p releases
cd docs
echo "== java/"; tar -cf - java/ | pigz -p 2 > ../releases/docs-java.tar.gz && echo JAVA_BUILT
echo "== sdks"; tar -cf - nodejs/ dotnet/ ruby/ python/ php/ go/ | pigz -p 2 > ../releases/docs-sdks.tar.gz && echo SDKS_BUILT
echo "== meta"; tar -cf - _meta/ | pigz -p 2 > ../releases/docs-meta.tar.gz && echo META_BUILT
echo "== core"; tar -cf - --exclude=./java --exclude=./nodejs --exclude=./dotnet --exclude=./ruby --exclude=./python --exclude=./php --exclude=./go --exclude=./_meta . | pigz -p 2 > ../releases/docs-core.tar.gz && echo CORE_BUILT
cd ../releases
for f in *.tar.gz; do gzip -t "$f" && echo "$f OK" || { echo "$f CORRUPT"; exit 1; }; done
echo ALL_ARCHIVES_READY
