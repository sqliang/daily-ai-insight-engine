CREATE TABLE "articles" (
	"id" text PRIMARY KEY NOT NULL,
	"source_dir" text NOT NULL,
	"created" date NOT NULL,
	"published" text,
	"url" text,
	"title" text,
	"author" text,
	"description" text,
	"tldr" text,
	"objective_summary" text,
	"event_type" text,
	"sentiment" text,
	"impact_score" numeric,
	"payload" jsonb NOT NULL,
	"updated_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "daily_reports" (
	"date" text PRIMARY KEY NOT NULL,
	"report" jsonb NOT NULL,
	"report_md" text,
	"generated_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "manifests" (
	"source" text NOT NULL,
	"date" text NOT NULL,
	"generated_at" timestamp with time zone,
	"payload" jsonb NOT NULL,
	CONSTRAINT "manifests_source_date_pk" PRIMARY KEY("source","date")
);
--> statement-breakpoint
CREATE INDEX "articles_source_created_idx" ON "articles" USING btree ("source_dir","created");--> statement-breakpoint
CREATE INDEX "articles_created_idx" ON "articles" USING btree ("created");--> statement-breakpoint
CREATE INDEX "articles_impact_score_idx" ON "articles" USING btree ("impact_score");