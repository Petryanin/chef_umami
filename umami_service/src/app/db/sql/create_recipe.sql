WITH ingredient_with_unit AS (
    SELECT
        unnest(cast(:ingredient_names as varchar(255)[])) AS ingredient_name,
        unnest(cast(:unit_short_names as varchar(50)[])) AS unit_short_name,
        unnest(cast(:unit_full_names as varchar(255)[])) AS unit_full_name,
        unnest(cast(:amounts as numeric[])) AS amount,
        unnest(cast(:sorts as smallint[])) AS sort
),
new_recipe AS (
    INSERT INTO
        recipe (
            name,
            description,
            instructions,
            cooking_time,
            servings,
            difficulty,
            category
        )
    VALUES
        (
            :recipe_name,
            :recipe_description,
            :recipe_instructions,
            :cooking_time,
            :servings,
            :difficulty,
            :category
        ) RETURNING recipe_id
),
_new_ingredient AS (
    INSERT INTO
        ingredient (name)
    SELECT
        ingredient_name
    FROM
        ingredient_with_unit
    ON CONFLICT (name) DO NOTHING
    RETURNING ingredient_id, name AS ingredient_name
),
new_ingredient AS (
    SELECT
        ingredient_id,
        ingredient_name
    FROM
        _new_ingredient
    UNION ALL
    SELECT
        ingredient_id,
        ingredient_name
    FROM
        ingredient
    JOIN ingredient_with_unit
        ON ingredient_with_unit.ingredient_name = ingredient.name
),
_new_unit AS (
    INSERT INTO
        unit (short_name, full_name)
    SELECT
        unit_short_name,
        unit_full_name
    FROM
        ingredient_with_unit
    ON CONFLICT (full_name) DO NOTHING
    RETURNING unit_id, full_name as unit_full_name
),
new_unit AS (
    SELECT
        unit_id,
        unit_full_name
    FROM
        _new_unit
    UNION ALL
    SELECT
        unit_id,
        full_name
    FROM
        unit
    WHERE
        full_name = ANY(
            ARRAY(
                SELECT
                    DISTINCT unit_full_name
                FROM
                    ingredient_with_unit
            )
        )
)
INSERT INTO
    recipe_ingredient (recipe_id, ingredient_id, unit_id, amount, sort)
SELECT
    new_recipe.recipe_id,
    new_ingredient.ingredient_id,
    new_unit.unit_id,
    ingredient_with_unit.amount,
    ingredient_with_unit.sort
FROM
    new_recipe
CROSS JOIN new_ingredient
JOIN ingredient_with_unit USING (ingredient_name)
JOIN new_unit USING (unit_full_name)
RETURNING recipe_id
