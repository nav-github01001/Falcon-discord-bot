CREATE TABLE "guild_settings"(
	"guild_id" INT NOT NULL UNIQUE PRIMARY KEY,
	"settings" JSON
);
CREATE TABLE "user_data"(
	"user_id" INT NOT NULL UNIQUE PRIMARY KEY,
	"wallet" INT,
	"bank_balance" INT,
	"items" JSON,
	"settings" JSON
	
);